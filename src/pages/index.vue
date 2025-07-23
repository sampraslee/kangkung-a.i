<template>
  <section id="user-welcome">
    <h1>Good afternoon, User</h1>
    <p>Welcome back, let's get you up to speed with your growing vegetables</p>
  </section>
  <hr />
  <section id="dashboard">
    <v-row>
      <v-col col="6">
        <ToDoCard></ToDoCard>
      </v-col>
      <v-col col="6">
        <InfoCard></InfoCard>
      </v-col>
    </v-row>
    <v-row>
      <v-col></v-col>
    </v-row>
  </section>
</template>

<script>
import ToDoCard from "@/components/ToDoCard.vue";
import InfoCard from "@/components/InfoCard.vue";
</script>
