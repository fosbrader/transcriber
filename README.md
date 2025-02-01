# Audio Transcriber

A simple web application that transcribes audio files using OpenAI's Whisper API. The application runs entirely in the browser and requires no server-side components.

## Features

- Drag and drop interface for audio files
- Supports multiple audio formats (.mp3, .wav, .m4a, .ogg)
- Real-time transcription using OpenAI's Whisper API
- Secure handling of API keys (never stored, only used locally)
- Clean, modern interface
- GitHub Actions integration for deployment

## Usage

1. Visit the [Audio Transcriber](https://fosbrader.github.io/transcriber) website
2. Choose one of two options for the API key:
   - Enter your personal OpenAI API key (get one from [OpenAI's website](https://platform.openai.com/api-keys))
   - Use the GitHub Actions secret (if deployed via GitHub)
3. Either drag and drop an audio file onto the dropzone or click to select a file
4. Wait for the transcription to complete
5. The transcribed text will appear below the dropzone

## Privacy & Security

- Your OpenAI API key is only used locally in your browser
- No data is stored on any servers
- Audio files are sent directly to OpenAI's API for transcription
- The application runs entirely client-side

## Deployment

### GitHub Pages Deployment

1. Fork or clone this repository: `git clone https://github.com/fosbrader/transcriber.git`
2. Go to your repository settings
3. Under "Security > Secrets and variables > Actions", add your OpenAI API key as `OPENAI_API_KEY`
4. Under "Pages", ensure the following settings:
   - Source: Deploy from a branch
   - Branch: gh-pages
5. Push to the main branch, and GitHub Actions will automatically deploy to Pages

### Local Development

To run this locally:

1. Clone the repository: `git clone https://github.com/fosbrader/transcriber.git`
2. Open `index.html` in your web browser
3. Enter your OpenAI API key
4. Start transcribing!

## License

MIT License - feel free to use, modify, and distribute as needed.

## Credits

Built using:
- OpenAI's Whisper API
- HTML5
- CSS3
- JavaScript
- GitHub Pages
- GitHub Actions 