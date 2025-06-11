<template>
  <div id="app">

    <VegeCard />

    <VegeTools />

    <VegeVideos />

    <div class="pagination">
      <span class="dot active"></span>
      <span class="dot"></span>
      <span class="dot"></span>
    </div>
        
    <button class="plant-button">I want to plant garlic</button>



  </div>
</template>

<script>
import VegeCard from './components/VegeCard.vue';
import VegeTools from './components/VegeTools.vue';
import VegeVideos from './components/VegeVideos.vue';

export default {
  name: 'App',
  components: {
    VegeCard, 
    VegeTools, 
    VegeVideos 
  }
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px; 
  background-color: #f0f0f0; 
  min-height: 100vh; 
  display: flex;
  flex-direction: column; 
  align-items: center; 
  padding-bottom: 20px; 
}

.header {
  width: 100%;
  padding: 20px 0;
  background-color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); 
  margin-bottom: 20px;
}

.header h1 {
  font-size: 1.5em; 
  color: #333;
}


.plant-button {
  background-color: #4CAF50; 
  color: white;
  padding: 15px 30px;
  border: none;
  border-radius: 25px; 
  font-size: 1.1em;
  cursor: pointer; 
  margin-top: 30px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
}

.plant-button:hover {
  background-color: #45a049; 
}

.pagination {
  display: flex; 
  justify-content: center;
  margin-top: 20px;
}

.dot {
  height: 10px;
  width: 10px;
  background-color: #bbb; 
  border-radius: 50%; 
  display: inline-block;
  margin: 0 5px; 
}

.dot.active {
  background-color: #717171; 
}

</style>