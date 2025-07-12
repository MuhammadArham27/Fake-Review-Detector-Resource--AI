import pandas as pd
import joblib
import json

with open("1.txt", "r", encoding="utf-8") as file:
    raw_data = file.read()

data = json.loads(raw_data)
results = data.get("results", [])

if results:
    df = pd.DataFrame(results)

    df = df[df["wrapperType"] == "audiobook"]
    df = df[df["description"].notna()]

    
    df['review'] = df.apply(lambda row: f"'{row['trackName']}' by {row['artistName']}' is a masterpiece from '{row['collectionName']}'. The lyrics and sound design are stunning.", axis=1)


    try:
        
        model = joblib.load(r"C:\Users\DELL\Desktop\doc\projects 1\model.pkl")
        vectorizer = joblib.load(r"C:\Users\DELL\Desktop\doc\projects 1\vectorizer.pkl")

     
        vectorized = vectorizer.transform(df["review"])
        df["prediction"] = model.predict(vectorized)
        
        genuine_df = df[df["prediction"] == 0]

        if not genuine_df.empty:
            print("\n✅ Genuine Reviews:")
            for _, row in genuine_df.iterrows():
                print(f"- {row['collectionName']}: {row['review'][:150]}...")
        else:
            print("⚠️ No genuine reviews found.")

    except Exception as e:
        print(f"❌ Error loading model or vectorizer: {e}")
else:
    print("⚠️ No results found in the loaded JSON.")
