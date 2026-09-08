import os
import subprocess
import sys
import zipfile

def check_java():
    try:
        subprocess.run(["java", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except (subprocess.SubprocessError, FileNotFoundError):
        print("Error: Java is required to run APKEditor and sign APKs. Please install Java and add it to your PATH.")
        sys.exit(1)

def download_apk_editor():
    jar_name = "APKEditor-1.4.2.jar"
    if not os.path.exists(jar_name):
        print(f"Downloading {jar_name}...")
        import urllib.request
        url = f"https://github.com/REAndroid/APKEditor/releases/download/V1.4.2/{jar_name}"
        urllib.request.urlretrieve(url, jar_name)
    return jar_name

def main():
    print("=== Peridot Local Revival - Automated APK Builder ===")
    check_java()
    
    jar_file = download_apk_editor()
    
    input_dir = input("Enter the path to the folder containing your split APKs (default current directory '.'): ").strip() or "."
    server_ip = input("Enter your local server IP (e.g., 192.168.0.120): ").strip()
    
    if not server_ip:
        print("Error: Server IP cannot be empty.")
        sys.exit(1)
        
    output_apk = "peridot_universal.apk"
    
    print("\n[1/4] Merging split APKs into universal package...")
    merge_cmd = ["java", "-jar", jar_file, "m", "-i", input_dir, "-o", output_apk]
    subprocess.run(merge_cmd, check=True)
    
    print("\n[2/4] Injecting custom api_key.txt...")
    os.makedirs("assets", exist_ok=True)
    with open(os.path.join("assets", "api_key.txt"), "w") as f:
        f.write(server_ip)
        
    with zipfile.ZipFile(output_apk, "a") as zip_ref:
        zip_ref.write(os.path.join("assets", "api_key.txt"), "assets/api_key.txt")
    
    print("\n[3/4] Generating debug keystore...")
    keystore_file = "debug.keystore"
    if not os.path.exists(keystore_file):
        keytool_cmd = [
            "keytool", "-genkey", "-v", "-keystore", keystore_file,
            "-storepass", "android", "-keypass", "android", "-alias", "androiddebugkey",
            "-keyalg", "RSA", "-keysize", "2048", "-validity", "10000",
            "-dname", "CN=Android Debug,O=Android,C=US"
        ]
        subprocess.run(keytool_cmd, check=True)
        
    print("\n[4/4] Signing universal APK...")
    sign_cmd = [
        "jarsigner", "-keystore", keystore_file,
        "-storepass", "android", "-keypass", "android",
        output_apk, "androiddebugkey"
    ]
    subprocess.run(sign_cmd, check=True)
    
    print(f"\nSuccess! Built and signed: {output_apk}")
    print("Transfer this file to your Android device, run your mock server, and launch the game.")

if __name__ == "__main__":
    main()
