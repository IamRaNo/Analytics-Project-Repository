import gdown
import pandas as pd
from sqlalchemy import create_engine

# -----------------------------
# 1. GOOGLE DRIVE DOWNLOAD
# -----------------------------

# Direct download URL (convert "view" link to "uc?id=")
file_id = "1tX_s5qfdOEDYcmGQN6SvlRm8-xolvpDF"
url = f"https://drive.google.com/uc?id={file_id}"

output_file = "meantal_health.csv"
gdown.download(url, output_file, quiet=False)


# -----------------------------
# 2. READ CSV
# -----------------------------
df = pd.read_csv(output_file, low_memory=False)


# -----------------------------
# 3. MYSQL CONNECTION
# -----------------------------
user = "root"
password = "7003890541"
host = "localhost"
port = "3306"
database = "mental_health_final_project"   # you said DB will already be created

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")


# -----------------------------
# 4. LOAD INTO MYSQL
# -----------------------------
table_name = "backup_mental_health"

df.to_sql(name=table_name, con=engine, if_exists="replace", index=False)

print(f"Table '{table_name}' imported successfully.")
