import os
import subprocess

SONAR_PATH = "/Users/abakhtin22/Documents/sonar-scanner-6.2.1.4610-macosx-x64/bin/sonar-scanner"
TOKEN = "sqa_bde2972ca3539cda86a01800002351995d20368e"


def run_sonarqube(project_path):
    project_name = os.path.basename(project_path)
    print(f"Inspecting {project_name}")

    # Create Understand project
    try:
        print(f"\t Analyzing Project...")
        subprocess.run([SONAR_PATH, f"-Dsonar.projectKey={project_name}", f"-Dsonar.token={TOKEN}",
                        f"-Dsonar.sources=./{project_name}", "-Dsonar.language=java",
                        "-Dsonar.host.url=http://localhost:9000", "-Dsonar.java.binaries=./fakedir"], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error while processing {project_name}: {e}")


def main(master_folder):

    project_folders = [f.path for f in os.scandir(master_folder) if f.is_dir()
                       and not f.path.endswith("code2dfd")
                       and not f.path.endswith("und")
                       and not f.path.endswith("jasome")
                       and not f.path.endswith("graph")
                       and not f.name in [".idea", ".git", "fakedir", ".scannerwork"]]
    for i, project in enumerate(project_folders, start=1):
        print(f"Progress: {i}/{len(project_folders)}")
        run_sonarqube(project)
        print("----------- \n")


if __name__ == "__main__":
    master_folder = os.getcwd()

    main(master_folder)