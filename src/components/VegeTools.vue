<template>
  <div class="vege-tools">
    <h3>What you'll need</h3>

    <div class="tool-item">
      <div class="tool-icon-placeholder"></div> <div class="tool-details">
        <h4>Soil</h4>
        <p>Describe the type of soil.</p>
      </div>
    </div>

    <div class="tool-item">
      <div class="tool-icon-placeholder"></div> <div class="tool-details">
        <h4>Fertilizer</h4>
        <p>Describe the type of fertilizer.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VegeTools'
};
</script>

<style scoped>

.vege-tools {
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin: 20px;
  width: 90%;
  max-width: 600px;
  text-align: left;
}

.vege-tools h3 {
  font-size: 1.6em;
  color: #333;
  margin-bottom: 15px;
}

.tool-item {
  display: flex; 
  align-items: center; 
  background-color: #f9f9f9; 
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); 
}

.tool-icon-placeholder {
  width: 50px;
  height: 50px;
  background-color: #e0e0e0; 
  border-radius: 8px;
  margin-right: 15px; 
}

.tool-details h4 {
  font-size: 1.2em;
  color: #333;
  margin: 0; 
}

.tool-details p {
  font-size: 0.9em;
  color: #777;
  margin: 5px 0 0 0; 
}
</style>