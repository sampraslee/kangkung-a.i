<template>
  <div class="vege-card">
    <div class="card-header">
      <span>Kangkung A.I</span>
      <span class="menu-icon">≡</span>
    </div>

    <img src="https://via.placeholder.com/150" alt="Garlic" class="garlic-image" />

    <div class="garlic-info-box">
      <h2 class="garlic-title">Garlic</h2>
      <p><span class="icon">⏰</span> Estimated time to harvest: <strong>2 - 6 weeks</strong></p>
      <p><span class="icon">💧</span> Water needs: <strong>Daily</strong></p>
      <p><span class="icon">☀️</span> Sunlight needs: <strong>1 - 2 hours a day</strong></p>
    </div>

    <div class="how-to-grow">
      <h3>How to grow</h3>
      <ol>
        <li>Choose a container or garden bed with good drainage.</li>
        <li>Fill with nutrient-rich, moist soil or compost.</li>
        <li>Sow seeds or plant cuttings about 1-2 inches deep.</li>
        <li>Keep the soil consistently moist, but not waterlogged.</li>
        <li>Place in an area receiving full sunlight (at least 6 hours daily).</li>
        <li>Harvest in 4-6 weeks by cutting the stems just above soil level, leaving roots intact for regrowth.</li>
      </ol>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VegeCard'
};
</script>

<style scoped>

.vege-card {
  background-color: white; 
  border-radius: 10px; 
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
  padding: 20px;
  margin: 20px;
  width: 90%; 
  max-width: 600px; 
  text-align: left; 
}

.card-header {
  display: flex; 
  justify-content: space-between; 
  align-items: center; 
  margin-bottom: 20px;
  font-weight: bold; 
  color: #555;
  font-size: 1.1em;
}

.menu-icon {
  font-size: 1.5em; 
  cursor: pointer;
}

.garlic-image {
  display: block; 
  margin: 0 auto 20px auto; 
  width: 150px; 
  height: 150px; 
  object-fit: cover; 
  border-radius: 50%; 
  background-color: #f0f0f0; 
}

.garlic-info-box {
  background-color: #e6ffe6; 
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 20px;
}

.garlic-title {
  font-size: 1.8em; 
  color: #333;
  margin-top: 0;
  margin-bottom: 10px;
}

.garlic-info-box p {
  margin: 8px 0; 
  color: #555;
  display: flex; 
  align-items: center;
}

.garlic-info-box .icon {
  margin-right: 8px; 
  font-size: 1.2em; 
  color: #4CAF50; 
}

.how-to-grow h3 {
  font-size: 1.6em;
  color: #333;
  margin-bottom: 15px;
}

.how-to-grow ol {
  padding-left: 20px; 
  color: #555;
  line-height: 1.6; 
}

.how-to-grow li {
  margin-bottom: 10px;
}
</style>