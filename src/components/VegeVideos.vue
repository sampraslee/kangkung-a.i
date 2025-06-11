<template>
  <div class="vege-videos">
    <h3>Videos for you</h3>

    <div class="video-item">
      <div class="video-thumbnail-placeholder">
        <span class="camera-icon">🎥</span> </div>
      <div class="video-details">
        <h4>Video title</h4>
        <p>Video duration</p>
        <p class="summary">This will be the A.I summary of the video.</p>
      </div>
    </div>

    </div>
</template>

<script>
export default {
  name: 'VegeVideos'
};
</script>

<style scoped>

.vege-videos {
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin: 20px;
  width: 90%;
  max-width: 600px;
  text-align: left;
}

.vege-videos h3 {
  font-size: 1.6em;
  color: #333;
  margin-bottom: 15px;
}

.video-item {
  display: flex; 
  align-items: center; 
  background-color: #f9f9f9;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.video-thumbnail-placeholder {
  width: 80px;
  height: 80px;
  background-color: #e0e0e0; 
  border-radius: 8px;
  margin-right: 15px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.camera-icon {
  font-size: 2em; 
  color: #777;
}

.video-details h4 {
  font-size: 1.2em;
  color: #333;
  margin: 0;
}

.video-details p {
  font-size: 0.9em;
  color: #777;
  margin: 5px 0 0 0;
}

.video-details .summary {
  font-size: 0.8em;
  color: #555;
  margin-top: 8px;
}
</style>