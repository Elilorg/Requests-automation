import subprocess
import xml.etree.ElementTree as ET
import os


def decompile_apk(apk_path, output_path):
    command = f"apktool d {apk_path} -o {output_path}"
    subprocess.run(command, shell=True, check=True)

def create_network_security_config(output_path):
    """Just adds the certificate src user to an exisiting file. Doesn't implement
        file creaton or editing anything else"""
    ns_config_path = os.path.join(output_path, "res", "xml", "network_security_config.xml")
    tree = ET.parse(ns_config_path)
    root = tree.getroot()

    # Find the location to add the new certificate element
    base_config = root.find('base-config')
    trust_anchors = base_config.find('trust-anchors')

    # Create the new certificate element
    new_certificate = ET.Element('certificates')
    new_certificate.set('src', 'user')
    #new_certificate.text = 'your_certificate_content'

    # Add the new certificate element to trust-anchors
    trust_anchors.append(new_certificate)

    # Serialize the modified XML back to a file
    tree.write(ns_config_path, encoding='utf-8', xml_declaration=True)


def modify_android_manifest(output_path):
    mainfest_path  = output_path + "/AndroidManifest.xml"

    tree = ET.ElementTree(file=output_path)
    root = tree.getroot()

    application = root.find("application")
    if application is None:
        application = ET.SubElement(root, "application")

    network_security_config = ET.SubElement(application, "android:networkSecurityConfig")
    network_security_config.set("resource", "xml/network_security_config")

    return application

def recompile_app(output_path) :
    app_name = "Youtubemode"
    command = f"apktool b {output_path} -o {app_name}.apk"
    subprocess.run(command, shell=True, check=True)
    command = f"apksigner sign --ks my-release-key.keystore {app_name}.apk"
    subprocess.run(command, shell=True, check=True)



if __name__ == "__main__":
    
    apk_path = "youtube-18-17-43.apk"
    decompile_apk(apk_path, "./Youtubapp")
    #apk_path = "original.apk"
    #output_path = "decompiled"
    #decompile_apk(apk_path, output_path)
    #
    #network_security_config = create_network_security_config("./Youtubapp")
    #recompile_app("Youtubapp")
    #modify_android_manifest(output_path)


