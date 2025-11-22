import RecordRTC from "recordrtc";

export function recordAudio() {
  return new Promise(async (resolve) => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

    const recorder = new RecordRTC(stream, {
      type: "audio",
      mimeType: "audio/wav",
    });

    recorder.startRecording();

    resolve({
      stop: () =>
        new Promise((resolveStop) => {
          recorder.stopRecording(() => {
            const blob = recorder.getBlob();
            resolveStop(blob);
          });
        }),
    });
  });
}
