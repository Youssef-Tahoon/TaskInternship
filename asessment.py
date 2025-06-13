from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Table_Input.csv')
    df = pd.read_csv(csv_path)

    
    # Process values for Table 2
    a5 = df.iloc[4, 1]  # A5 is 5th row, 2nd column (0-indexed)
    a7 = df.iloc[6, 1]
    a12 = df.iloc[11, 1]
    a13 = df.iloc[12, 1]
    a15 = df.iloc[14, 1]
    a20 = df.iloc[19, 1]

    table2 = {
        'Alpha': a5 + a20,
        'Beta': a15 / a7 if a7 != 0 else 'Undefined',
        'Charlie': a13 * a12
    }
    return render_template('index.html', table1=df.to_html(index=False), table2=table2)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)