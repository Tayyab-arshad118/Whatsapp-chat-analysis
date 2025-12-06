# WhatsApp Chat Analyzer 📊

Analyze your WhatsApp conversations with detailed insights into messaging patterns, word usage, emoji statistics, and activity trends.

🔗 **[Try it live here!](https://whatsuuup-chat-analyzer.streamlit.app/)**

## Features

- 📊 **Statistics**: Message count, word count, media & links shared
- 📅 **Timelines**: Monthly/daily activity patterns with heatmaps
- 👥 **User Analysis**: Most active members in group chats
- 💬 **Word Cloud**: Visual representation of frequently used words
- 😊 **Emoji Analysis**: Most used emojis with charts

## Installation

```bash
git clone <your-repo-url>
cd whatsapp-chat-analyzer
pip install -r requirements.txt
streamlit run app.py
```

## Usage

1. **Export your WhatsApp chat**
   - Android: Chat → ⋮ → More → Export chat → Without media
   - iPhone: Chat → Contact name → Export Chat → Without Media

2. **Upload the `.txt` file** to the analyzer

3. **Select a user** or "Overall" for group analysis

4. **Click "Show Analysis"** to view insights

## Project Structure

```
├── app.py              # Main application
├── preprocess.py       # Data preprocessing
├── helper.py           # Analysis functions
├── romanEng2.txt       # Stop words (Roman Urdu/English)
└── requirements.txt    # Dependencies
```

## Requirements

- Python 3.7+
- streamlit
- matplotlib, seaborn
- pandas
- wordcloud, emoji, urlextract

## How It Works

1. Parses WhatsApp chat export format: `MM/DD/YY, HH:MM AM/PM - User: Message`
2. Extracts temporal features (year, month, day, hour)
3. Filters stop words and analyzes word frequency
4. Generates visualizations and statistics

## Contributing

Contributions welcome! Open an issue or submit a pull request.

## License

MIT License

---

Built with ❤️ using [Streamlit](https://streamlit.io/)

## Features ✨

### 📈 Statistical Analysis
- **Total Messages**: Count of all messages in the chat
- **Total Words**: Word count across all messages
- **Media Shared**: Number of media files shared
- **Links Shared**: Count of URLs shared in conversations

### 📅 Timeline Analysis
- **Monthly Timeline**: Visualize message frequency over months
- **Daily Timeline**: Track daily messaging patterns
- **Activity Maps**: 
  - Most busy day of the week
  - Most busy month
  - Weekly activity heatmap showing hourly patterns

### 👥 User Analysis
- **Most Active Users**: Bar chart and percentage breakdown of top contributors
- Available when analyzing the overall group chat

### 💬 Content Analysis
- **Word Cloud**: Visual representation of most frequently used words
- **Most Common Words**: Bar chart of top 20 most used words
- **Emoji Analysis**: 
  - Table of most used emojis with counts
  - Pie chart visualization of top emojis

## Installation 🚀

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd whatsapp-chat-analyzer
```

2. **Install required dependencies**
```bash
pip install -r requirements.txt
```

### Dependencies
```
streamlit
matplotlib
seaborn
urlextract
wordcloud
pandas
emoji
```

## Usage 💻

### 1. Export Your WhatsApp Chat

**For Android:**
1. Open the chat you want to analyze
2. Tap the three dots (⋮) in the top right
3. Select "More" → "Export chat"
4. Choose "Without media"
5. Save the `.txt` file

**For iPhone:**
1. Open the chat you want to analyze
2. Tap the contact/group name at the top
3. Scroll down and tap "Export Chat"
4. Choose "Without Media"
5. Save the `.txt` file

### 2. Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### 3. Analyze Your Chat

1. Click "Browse files" in the sidebar
2. Upload your WhatsApp chat `.txt` file
3. Select a user from the dropdown or choose "Overall" for group analysis
4. Click "Show Analysis" button
5. Explore the various visualizations and statistics

## Project Structure 📁

```
whatsapp-chat-analyzer/
│
├── app.py                 # Main Streamlit application
├── preprocess.py          # Chat data preprocessing module
├── helper.py              # Analysis and visualization functions
├── romanEng2.txt          # Stop words file (Roman Urdu & English)
├── requirements.txt       # Python dependencies
├── data-analysis.ipynb    # Jupyter notebook for development/testing
└── README.md             # This file
```

## How It Works 🔧

### Data Processing Pipeline

1. **File Upload**: User uploads WhatsApp chat export file
2. **Preprocessing** (`preprocess.py`):
   - Extracts timestamps and messages using regex patterns
   - Separates user names from message content
   - Creates structured DataFrame with temporal features (year, month, day, hour, etc.)
3. **Analysis** (`helper.py`):
   - Performs statistical calculations
   - Generates visualizations
   - Filters stop words for meaningful word analysis
4. **Visualization** (`app.py`):
   - Displays interactive Streamlit dashboard
   - Shows charts, graphs, and statistics

### Supported Chat Format

The analyzer supports the standard WhatsApp export format:
```
MM/DD/YY, HH:MM AM/PM - Username: Message
```

Example:
```
10/09/24, 8:22 PM - John Doe: Hello everyone!
```

## Features in Detail 🔍

### Statistical Insights
- Real-time calculation of message counts, word counts, media sharing frequency
- URL extraction and counting
- User-specific or group-wide analysis

### Temporal Analysis
- Monthly and daily message trends
- Day-of-week activity patterns
- Hour-by-hour heatmap showing peak activity times

### Text Analysis
- Stop words filtering (supports Roman Urdu and English)
- Word frequency analysis excluding common words
- Visual word clouds for quick content overview

### Emoji Analytics
- Most frequently used emojis with counts
- Visual representation through pie charts
- Support for all Unicode emojis

## Customization 🎨

### Adding Custom Stop Words

Edit `romanEng2.txt` to add or remove stop words:
```
word1
word2
word3
```

### Modifying Visualizations

In `app.py`, you can customize:
- Chart colors
- Figure sizes
- Number of top items displayed
- Layout and styling

## Limitations ⚠️

- Supports only text-based analysis (media files are counted but not analyzed)
- Works with standard WhatsApp export format only
- Stop words file is optimized for Roman Urdu and English
- Large chat files may take longer to process

## Troubleshooting 🔧

### Common Issues

1. **"No module named 'streamlit'"**
   - Solution: Run `pip install -r requirements.txt`

2. **Chat file not being processed**
   - Ensure the file is in `.txt` format
   - Check that the chat format matches the expected pattern
   - Verify the date format is MM/DD/YY

3. **Visualizations not showing**
   - Ensure matplotlib and seaborn are properly installed
   - Check browser console for errors
   - Try refreshing the page

## Contributing 🤝

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## License 📄

This project is open source and available under the MIT License.

## Acknowledgments 🙏

- Built with [Streamlit](https://streamlit.io/)
- Visualizations powered by [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/)
- Word cloud generation using [WordCloud](https://github.com/amueller/word_cloud)
- Emoji support from [emoji](https://github.com/carpedm20/emoji/) library

## Contact 📧

For questions, suggestions, or issues, please open an issue on the GitHub repository.

---

**Happy Analyzing! 📊✨**
