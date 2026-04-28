<a id="top"></a>

<h1 align="center">🌿 Sugarcane Leaf Disease Detection</h1>
<h3 align="center">AI-Based Disease Detection using Deep Learning & Image Processing</h3>

<p align="center">
  <img src="Report&PPT/banner.png" width="80%" alt="Banner"/>
</p>

<hr>

<h2>📌 Table of Contents</h2>
<ul>
  <li><a href="#introduction">Introduction</a></li>
  <li><a href="#problem">Problem Statement</a></li>
  <li><a href="#objectives">Objectives</a></li>
  <li><a href="#methodology">Methodology</a></li>
  <li><a href="#features">Features</a></li>
  <li><a href="#dataset">Dataset</a></li>
  <li><a href="#architecture">Model Architecture</a></li>
  <li><a href="#results">Results</a></li>
  <li><a href="#run">How to Run</a></li>
  <li><a href="#structure">Project Structure</a></li>
  <li><a href="#future">Future Improvements</a></li>
  <li><a href="#team">Team Details</a></li>
  <li><a href="#abstract">Research Abstract</a></li>
</ul>

<hr>

<h2 id="introduction">📖 Introduction</h2>
<p>
Sugarcane productivity is affected by diseases like rust, red rot, smut, and yellow leaf disease.
Manual detection is slow, error-prone, and not scalable.
</p>

<p>
This project introduces an <b>AI-powered system</b> using <b>CNNs</b> for accurate disease detection.
</p>

<hr>

<h2 id="problem">❗ Problem Statement</h2>
<ul>
  <li>Manual detection is slow and inaccurate</li>
  <li>Farmers lack automated tools</li>
  <li>Late detection causes crop loss</li>
  <li>Environmental variations affect accuracy</li>
</ul>

<p><b>Goal:</b> Build an automated, scalable detection system</p>

<hr>

<h2 id="objectives">🎯 Objectives</h2>
<ul>
  <li>Develop CNN-based model</li>
  <li>Enable early detection</li>
  <li>Improve real-world accuracy</li>
  <li>Use data augmentation</li>
  <li>Evaluate with Precision, Recall, F1-score</li>
</ul>

<hr>

<h2 id="methodology">🧠 Methodology</h2>
<ol>
  <li><b>Data Collection:</b> Annotated dataset</li>
  <li><b>Preprocessing:</b> Noise removal, segmentation</li>
  <li><b>Training:</b> CNN + augmentation</li>
  <li><b>Evaluation:</b> Accuracy, Precision, Recall</li>
</ol>

<hr>

<h2 id="features">✨ Features</h2>
<ul>
  <li>✔ CNN-based classification</li>
  <li>✔ Data augmentation</li>
  <li>✔ Confusion matrix</li>
  <li>✔ Accuracy & loss graphs</li>
</ul>

<hr>

<h2 id="dataset">📂 Dataset</h2>

<pre>
dataset/
  train/
    healthy/
    rust/
    red_rot/
    yellow/
  val/
    healthy/
    rust/
    red_rot/
    yellow/
</pre>

<hr>

<h2 id="architecture">🏗️ Model Architecture</h2>
<ul>
  <li>3 Convolution Layers + MaxPooling</li>
  <li>Dense Layers</li>
  <li>Dropout</li>
  <li>Softmax Output</li>
</ul>

<hr>

<h2 id="results">📊 Results</h2>
<ul>
  <li>Training Accuracy: ~99%</li>
  <li>Validation Accuracy: ~93%</li>
  <li>Balanced Precision, Recall, F1-score</li>
</ul>

<hr>

<h2 id="run">▶️ How to Run</h2>

<pre>
pip install -r requirements.txt
python src/train.py
python src/evaluate.py
</pre>

<hr>

<h2 id="structure">📁 Project Structure</h2>

<pre>
sugarcane-disease-detection/
│
├── dataset/
├── Source Code/
│   ├── src/
│   ├── outputs/
├── documentation/
│   └── abstract.pdf
├── README.md
</pre>

<hr>

<h2 id="future">🚀 Future Improvements</h2>
<ul>
  <li>Use ResNet / EfficientNet</li>
  <li>Add spectral imaging</li>
  <li>Deploy with Streamlit</li>
  <li>Mobile integration</li>
</ul>

<hr>

<h2 id="team">👨‍👩‍👧‍👦 Team Details</h2>

<table border="1" cellpadding="8">
<tr>
<th>Name</th>
<th>Program</th>
<th>University</th>
<th>Email</th>
</tr>

<tr>
<td>Yash Goyal</td>
<td>B.E (CSE)</td>
<td>Chitkara University</td>
<td>yash2555.be22@chitkara.edu.in</td>
</tr>

<tr>
<td>Himanshi</td>
<td>B.E (CSE)</td>
<td>Chitkara University</td>
<td>himanshi1656.be22@chitkara.edu.in</td>
</tr>

<tr>
<td>Vanshika Garg</td>
<td>B.E (CSE)</td>
<td>Chitkara University</td>
<td>vanshika2507.be22@chitkara.edu.in</td>
</tr>

<tr>
<td>Shreyas Sharma</td>
<td>B.E (CSE)</td>
<td>Chitkara University</td>
<td>shreyas2346.be22@chitkara.edu.in</td>
</tr>

</table>

<hr>

<h2 id="abstract">📄 Research Abstract</h2>

<p>
📎 <b>View Full Abstract:</b><br>
<a href="Report&PPT/Abstract_Integrative Analysis and Detection of Sugarcane Leaf Diseases Using Advanced Machine Learning and Image Processing Techniques.docx">Open Abstract Document</a>
</p>

<p><b>Summary:</b></p>
<ul>
  <li>AI-based sugarcane disease detection</li>
  <li>CNN + Image Processing</li>
  <li>High accuracy & scalable system</li>
</ul>

<hr>

<p align="center">
  <a href="#top">⬆ Back to Top</a>
</p>
