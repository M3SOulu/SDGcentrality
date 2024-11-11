import os
import subprocess

JASOME_PATH = "/Users/abakhtin22/Documents/jasome-0.6.8-alpha/bin/jasome"


def run_understand(project_path, output_dir):
    """Run SciTools Understand on the given project path and output results to a CSV file."""
    project_name = os.path.basename(project_path)
    print(f"Inspecting {project_name}")

    # Create Understand project
    try:
        print(f"\t Analyzing Project...")
        subprocess.run([JASOME_PATH, project_path, "--output", output_dir], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error while processing {project_name}: {e}")


def main(master_folder):

    project_folders = [f.path for f in os.scandir(master_folder) if f.is_dir()
                       and not f.path.endswith("code2dfd")
                       and not f.path.endswith("und")
                       and not f.path.endswith("jasome")
                       and not f.name in [".idea", ".git"]]
    analyze_folder = []
    output_files = []
    for project in project_folders:
        for root, dirs, files in os.walk(project):
            if "src" in dirs:
                analyze_folder.append(os.path.join(project, root, "src"))
                output_files.append(f"{os.path.basename(project)}-jasome/{os.path.basename(root)}.xml")

    for i, (project, output) in enumerate(zip(analyze_folder, output_files), start=1):
        print(f"Progress: {i}/{len(analyze_folder)}")
        os.makedirs(os.path.dirname(output), exist_ok=True)
        run_understand(project, output)
        print("----------- \n")


if __name__ == "__main__":
    master_folder = os.getcwd()

    main(master_folder)