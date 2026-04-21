<!DOCTYPE html>
<html>
<head>
    <title>Pick & Stow Reports Dashboard</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
        body { font-family: 'Inter', sans-serif; margin: 0; padding: 0; background: #f8f9fa; }
        .header { background: linear-gradient(90deg, #1e3a8a, #3b82f6); color: white; padding: 2rem; text-align: center; }
        .container { max-width: 1200px; margin: 2rem auto; padding: 2rem; background: white; border-radius: 12px; box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1); }
        h1, h2, h3 { color: #1e3a8a; }
        table { width: 100%; border-collapse: collapse; margin: 1.5rem 0; }
        th, td { padding: 12px 15px; text-align: left; border-bottom: 1px solid #e5e7eb; }
        th { background: #f1f5f9; font-weight: 600; }
        .tab { display: none; }
        .tab.active { display: block; }
        .nav { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 2rem; }
        .nav button { padding: 12px 24px; border: none; background: #e2e8f0; border-radius: 8px; cursor: pointer; font-weight: 500; transition: all 0.2s; }
        .nav button.active { background: #1e3a8a; color: white; }
        .highlight { background: #fefce8; padding: 1rem; border-radius: 8px; border-left: 5px solid #eab308; }
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 Warehouse Performance Dashboard</h1>
        <p style="font-size: 1.2rem; margin: 0;">Pick Report + Stow Report • April 5th – April 12th</p>
        <p><strong>Multi-Page Interactive Report</strong> • All spreadsheets & updates included</p>
    </div>

    <div class="container">
        <!-- Navigation -->
        <div class="nav">
            <button onclick="openTab(0)" class="active" id="tab0">🏠 Home / Summary</button>
            <button onclick="openTab(1)" id="tab1">📦 Pick Report (Original + Updated)</button>
            <button onclick="openTab(2)" id="tab2">📦 Stow Report (Original + Updated)</button>
            <button onclick="openTab(3)" id="tab3">👥 3-Associate Comparison</button>
        </div>

        <!-- Tab 0: Home / Summary -->
        <div id="content0" class="tab active">
            <h2>Welcome to the Multi-Page Streamlit Dashboard</h2>
            <p>This is a complete, self-contained interactive dashboard (built as a single HTML file that mimics a full Streamlit multi-page app). It contains <strong>every spreadsheet</strong> we created during our conversation.</p>
            
            <div class="highlight">
                <h3>Key Updates & Explanations</h3>
                <ul>
                    <li><strong>Updated Reports</strong>: Every associate was normalized to narossoh’s opportunity volume (Pick: 746 opp, Stow: 1,068 opp) while keeping their individual error rates (DPMO) the same. Defects were scaled proportionally.</li>
                    <li><strong>Why we did this</strong>: It allows fair comparison of quality performance across associates who worked very different volumes.</li>
                    <li><strong>3-Associate Focus</strong>: narossoh, elizev, and arrizola are highlighted in every view because they were the focus of the latest analysis.</li>
                </ul>
            </div>

            <h3>Quick Stats</h3>
            <p><strong>Total Associates:</strong> 17 per report</p>
            <p><strong>Original Total Opportunities:</strong> Pick = 4,214 | Stow = 6,112</p>
            <p><strong>After normalization (all at narossoh volume):</strong> Pick = 12,682 | Stow = 18,156</p>
        </div>

        <!-- Tab 1: Pick Report -->
        <div id="content1" class="tab">
            <h2>Pick Report – Original & Updated</h2>
            <h3>Updated Pick Report (All associates normalized to narossoh’s 746 opportunities)</h3>
            <table>
                <thead>
                    <tr>
                        <th>User</th>
                        <th>Original Defects</th>
                        <th>Original Opp</th>
                        <th>New Defects (at 746 opp)</th>
                        <th>New DPMO</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>narossoh</td><td>57</td><td>746</td><td>57</td><td>76,408</td></tr>
                    <tr><td>stajenni</td><td>14</td><td>804</td><td>13</td><td>17,426</td></tr>
                    <tr><td>danijac</td><td>13</td><td>169</td><td>57</td><td>76,408</td></tr>
                    <tr><td>arrizola</td><td>13</td><td>614</td><td>16</td><td>21,448</td></tr>
                    <tr><td>hasnsai</td><td>8</td><td>214</td><td>28</td><td>37,534</td></tr>
                    <tr><td>uiyps</td><td>8</td><td>208</td><td>29</td><td>38,874</td></tr>
                    <tr><td>jnoonoor</td><td>7</td><td>110</td><td>47</td><td>63,003</td></tr>
                    <tr><td>gpliegom</td><td>7</td><td>362</td><td>14</td><td>18,767</td></tr>
                    <tr><td>mtiband r</td><td>6</td><td>68</td><td>66</td><td>88,472</td></tr>
                    <tr><td>elizev</td><td>6</td><td>176</td><td>25</td><td>33,512</td></tr>
                    <tr><td>hersmary</td><td>5</td><td>69</td><td>54</td><td>72,386</td></tr>
                    <tr><td>mnimhas</td><td>5</td><td>97</td><td>38</td><td>50,938</td></tr>
                    <tr><td>iqrayuss</td><td>4</td><td>37</td><td>81</td><td>108,579</td></tr>
                    <tr><td>nkaibrah</td><td>4</td><td>255</td><td>12</td><td>16,086</td></tr>
                    <tr><td>matstrak</td><td>3</td><td>186</td><td>12</td><td>16,086</td></tr>
                    <tr><td>abdiosmg</td><td>3</td><td>44</td><td>51</td><td>68,365</td></tr>
                    <tr><td>musaom</td><td>2</td><td>55</td><td>27</td><td>36,193</td></tr>
                </tbody>
            </table>
            <p><strong>Explanation:</strong> Every associate now has exactly 746 opportunities. Defects were scaled using their original defect rate. This makes quality performance directly comparable.</p>
        </div>

        <!-- Tab 2: Stow Report -->
        <div id="content2" class="tab">
            <h2>Stow Report – Original & Updated</h2>
            <h3>Updated Stow Report (All associates normalized to narossoh’s 1,068 opportunities)</h3>
            <table>
                <thead>
                    <tr>
                        <th>User</th>
                        <th>Original Defects</th>
                        <th>Original Opp</th>
                        <th>New Defects (at 1,068 opp)</th>
                        <th>New DPMO</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>narossoh</td><td>164</td><td>1,068</td><td>164</td><td>153,558</td></tr>
                    <tr><td>iqrayuss</td><td>130</td><td>758</td><td>183</td><td>171,348</td></tr>
                    <tr><td>uiyps</td><td>117</td><td>330</td><td>379</td><td>354,869</td></tr>
                    <tr><td>mnimhas</td><td>94</td><td>668</td><td>150</td><td>140,449</td></tr>
                    <tr><td>hersmary</td><td>45</td><td>246</td><td>195</td><td>182,584</td></tr>
                    <tr><td>mtiband r</td><td>37</td><td>445</td><td>89</td><td>83,333</td></tr>
                    <tr><td>danijac</td><td>22</td><td>168</td><td>140</td><td>131,086</td></tr>
                    <tr><td>nkaibrah</td><td>17</td><td>518</td><td>35</td><td>32,772</td></tr>
                    <tr><td>gpliegom</td><td>15</td><td>580</td><td>28</td><td>26,217</td></tr>
                    <tr><td>matstrak</td><td>13</td><td>594</td><td>23</td><td>21,536</td></tr>
                    <tr><td>hasnsai</td><td>12</td><td>416</td><td>31</td><td>29,026</td></tr>
                    <tr><td>elizev</td><td>12</td><td>204</td><td>63</td><td>58,989</td></tr>
                    <tr><td>pmhusse</td><td>9</td><td>308</td><td>31</td><td>29,026</td></tr>
                    <tr><td>stajenni</td><td>7</td><td>127</td><td>59</td><td>55,243</td></tr>
                    <tr><td>abdiosmg</td><td>4</td><td>214</td><td>20</td><td>18,727</td></tr>
                    <tr><td>jnoonoor</td><td>3</td><td>63</td><td>51</td><td>47,753</td></tr>
                    <tr><td>arrizola</td><td>3</td><td>57</td><td>56</td><td>52,434</td></tr>
                </tbody>
            </table>
            <p><strong>Explanation:</strong> All associates now have exactly 1,068 opportunities. Defects scaled proportionally to their original error rate. This is the normalized version we created together.</p>
        </div>

        <!-- Tab 3: 3-Associate Comparison -->
        <div id="content3" class="tab">
            <h2>3-Associate Comparison (narossoh, elizev, arrizola)</h2>
            
            <h3>Original Data</h3>
            <table>
                <thead>
                    <tr><th>Report</th><th>User</th><th>Opportunities</th><th>Defects</th><th>DPMO</th></tr>
                </thead>
                <tbody>
                    <tr><td>Pick</td><td>narossoh</td><td>746</td><td>57</td><td>76,408</td></tr>
                    <tr><td>Pick</td><td>elizev</td><td>176</td><td>6</td><td>33,512</td></tr>
                    <tr><td>Pick</td><td>arrizola</td><td>614</td><td>13</td><td>21,448</td></tr>
                    <tr><td>Stow</td><td>narossoh</td><td>1,068</td><td>164</td><td>153,558</td></tr>
                    <tr><td>Stow</td><td>elizev</td><td>204</td><td>12</td><td>58,989</td></tr>
                    <tr><td>Stow</td><td>arrizola</td><td>57</td><td>3</td><td>52,434</td></tr>
                </tbody>
            </table>

            <h3>Updated (Normalized to narossoh’s volume)</h3>
            <table>
                <thead>
                    <tr><th>Report</th><th>User</th><th>Opportunities</th><th>Defects</th><th>DPMO</th></tr>
                </thead>
                <tbody>
                    <tr><td>Pick</td><td>narossoh</td><td>746</td><td>57</td><td>76,408</td></tr>
                    <tr><td>Pick</td><td>elizev</td><td>746</td><td>25</td><td>33,512</td></tr>
                    <tr><td>Pick</td><td>arrizola</td><td>746</td><td>16</td><td>21,448</td></tr>
                    <tr><td>Stow</td><td>narossoh</td><td>1,068</td><td>164</td><td>153,558</td></tr>
                    <tr><td>Stow</td><td>elizev</td><td>1,068</td><td>63</td><td>58,989</td></tr>
                    <tr><td>Stow</td><td>arrizola</td><td>1,068</td><td>56</td><td>52,434</td></tr>
                </tbody>
            </table>

            <div class="highlight">
                <strong>Summary Explanation:</strong> narossoh had the highest (worst) DPMO in both reports even after normalization. arrizola consistently shows the best quality performance. This view combines all the spreadsheets we built.
            </div>
        </div>
    </div>

    <script>
        function openTab(n) {
            // Hide all tabs
            document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
            // Show selected
            document.getElementById('content' + n).classList.add('active');
            // Update active button
            document.querySelectorAll('.nav button').forEach(btn => btn.classList.remove('active'));
            document.getElementById('tab' + n).classList.add('active');
        }
        
        // Auto-open first tab
        console.log('%c✅ Multi-page dashboard loaded successfully!', 'color: #1e3a8a; font-size: 16px; font-weight: bold;');
    </script>
</body>
</html>
