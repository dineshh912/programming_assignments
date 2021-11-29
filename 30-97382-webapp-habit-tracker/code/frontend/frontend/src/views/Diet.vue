<template>
  <section class="mt-3">
    <div class="row">
        <div class="col-6">
            <h5>Food </h5>
            <div class="mb-3">
              <textarea name="input" v-model="foods" class="form-control" placeholder="Enter Food name"></textarea>
              <span class="">Enter food items, seperated by comma ex: 1cup rice, 200g ice cream etc.,</span>
            </div>
            <button type="submit" class="btn btn-primary" @click="find_nutrition_value(foods)">Find nutrition Value</button>
            <button type="submit" class="btn btn-primary m-3" >Get Recepie</button>
        </div>

         <div class="col-6">    
            <h5>Liked Items</h5>
        </div>
    </div>
  </section>
</template>
<script>

import axios from 'axios';

export default {
  name: 'Diet',
  data(){
      return {
          nutritionURL: "https://api.edamam.com/api/nutrition-data",
          appID:"d9a8d3d2",
          appKey:"1abf30192c308a5611926b8c424bc159",
          foods:""

      }
  },
  computed : {
  },
  methods:{
      find_nutrition_value(food){
        // construct API URL
        var url = `${this.nutritionURL}?app_id=${this.appID}&app_key=${this.appKey}&nutrition-type=cooking&ingr=${food}`
        // API Request
        axios.get(url)
        .then(response => (console.log(response.data.calories)));

      }
      
  }
}
</script>