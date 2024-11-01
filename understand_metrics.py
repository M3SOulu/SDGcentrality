import os
import subprocess
import csv
import shutil


# using time module
import time

UND_PATH = "/Applications/Understand.app/Contents/MacOS/und"
def get_project_folders(master_folder):
    """Get a list of all subfolders in the master folder."""
    return [f.path for f in os.scandir(master_folder) if f.is_dir()]

def run_understand(project_path, output_dir):
    """Run SciTools Understand on the given project path and output results to a CSV file."""
    project_name = os.path.basename(project_path)
    print(f"Inspecting {project_name}")
    output_file = os.path.join(output_dir, f"all_metrics.csv")

    # Create Understand project
    udb_path = os.path.join(output_dir, f"{project_name}")
    udb_file = os.path.join(output_dir, f"{project_name}.und")
    try:
        print(f"\t Creating Understand Project at {udb_path}")
        subprocess.run(["und", "create", "-languages", "all", udb_path], check=True)
        print(f"\t Adding Projects File... from path {project_path}")
        subprocess.run(["und", "add", project_path, udb_file], check=True)
        #print(f"\t Setting generation of all metrics")
        #subprocess.run(["und", "settings", "-metrics", "all", udb_file], check=True)
        print(f"\t Analyzing Project...")
        subprocess.run(["und", "analyze", udb_file], check=True)
        print(f"\t ...Done")

        # Extract metrics
        print(f"\t Generating Metrics")
        result = subprocess.run(["und", "metrics", udb_file], capture_output=True, text=True, check=True)
        print(result.stdout)
        print(f"\t Metrics Available at {udb_file}")
        #os.rename(output_file,f"{project_name}.csv")

    except subprocess.CalledProcessError as e:
        print(f"Error while processing {project_name}: {e}")

    # Clean up .udb file
    shutil.rmtree(udb_file, ignore_errors=True)


def main(master_folder, output_dir, start_project=None):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    project_folders = get_project_folders(master_folder)
    if start_project:
        project_folders = project_folders[project_folders.index(start_project):]

    i = 1
    for project in project_folders:
        # ts stores the time in seconds
        ts = time.time()
        print(f"({ts}) - Progress: {i}/{len(project_folders)}")
        run_understand(project, output_dir)
        i += 1
        print("----------- \n")


if __name__ == "__main__":
    master_folder = "/Users/abakhtin22/Documents/TempNet/SDGcentrality/java-microservics"
    output_dir = "/Users/abakhtin22/Documents/TempNet/SDGcentrality"


    start_project_path = "gitsome"
    start_project_path = os.path.join(master_folder, start_project_path)

    main(master_folder, output_dir, start_project_path)
