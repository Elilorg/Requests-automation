from midiutil.MidiFile import MIDIFile
from midiutil import readFile
from music21 import note as objet_note
from music21 import *

# Ouvrez le fichier MIDI à analyser
# Récupère les notes de la première piste

mf = readFile("nom_du_fichier.mid")[0]

notes = mf.getNotes(0)

# Créez une table de correspondance entre les valeurs MIDI des toniques et leurs noms
tonic_names = {60: "Do", 62: "Ré", 64: "Mi", 65: "Fa", 67: "Sol", 69: "La", 71: "Si"}


###         pitch, duration, start_time, volume = note

# Récupère la durée de la dernière note de la piste
last_note_end = notes[-1][2] + notes[-1][1]

# Créez un objet Stream contenant les notes de la piste
stream = stream.Stream()
for pitch, duration, start_time, volume in notes:
  note = note.Note(pitch)
  note.duration.quarterLength = duration
  note.offset = start_time
  stream.append(note)

# Récupère les notes jouées pendant les 2 dernières secondes de la piste
final_notes = stream.getElementsByOffset(last_note_end - 2, last_note_end, includeEndBoundary=True)

# Créez un objet Chord à partir des notes de l'accord final
final_chord = chord.Chord(final_notes)

# Si l'accord final est majeur, utilisez la note la plus haute de l'accord comme tonique
if final_chord.isMajorTriad():
  tonic = final_chord.pitches[-1].midi

# Si l'accord final est mineur, utilisez la note la plus basse de l'accord comme tonique
else:
  tonic = final_chord.pitches[0].midi

# Créez une liste des fréquences d'apparition de chaque note de l'échelle diatonique dans la piste
scale_counts = [0] * 7

for pitch, duration, start_time, volume in notes:
  # Normalise la note par rapport à la tonique
  pitch -= tonic
  while pitch < 0:
    pitch += 12
  while pitch >= 12:
    pitch -= 12

  # Incrémente le compteur de la note de l'échelle diatonique correspondante
  scale_counts[pitch % 7] += 1

# Trouvez la note de l'échelle diatonique qui apparaît le plus souvent dans la piste
most_common_note = max(scale_counts)

# Détermine la tonalité en fonction de la note la plus fréquemment utilisée et de la tonique
if scale_counts.index(most_common_note) in [1, 2]:
  tonality = f"{tonic_names[tonic]}m"
else:
  tonality = tonic_names[tonic]

# Affiche la tonalité de la piste à l'écran
print(f"La tonalité de la piste est {tonality}.")
