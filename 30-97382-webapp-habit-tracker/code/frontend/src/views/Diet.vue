<template>
  <section class="mt-3">
    <div class="row">
        <div class="col-12">
          <ul class="nav nav-pills">
            <li class="nav-item">
              <a class="nav-link" href="#" @click="change_status('nut')">Nutrition Value</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#" @click="change_status('food')">Food Recipe</a>
            </li>
          </ul>
          
            <div class="mb-3 mt-3" v-if="nutrition">
              <div class="form-element">
                <textarea name="input" v-model="foods" class="form-control" placeholder="Enter Food name"></textarea>
                <span class="">Enter food items, seperated by comma ex: 1cup rice, 200g ice cream etc.,</span><br/>
                <button type="submit" class="btn btn-primary mt-1" 
                        @click="find_nutrition_value(foods)">Find nutrition Value</button>
              </div>
              <div class="result mt-3" v-if='nutritionList !=""'>
                  <span> calories: <strong>{{ nutritionList.calories }}</strong></span><br/>
                  <span> Diet Labels: <strong>{{ nutritionList.dietLabels }}</strong></span><br/>

                  <table class="table table-hover">
                    <thead>
                      <tr>
                        <td> Label </td>
                        <td> Qty </td>
                        <td> Unit </td>
                      </tr>
                    </thead>
                    <tbody>

                      <tr v-for="item in nutritionList.totalNutrients" 
                                :key="item.id">
                        <td>{{item.label}}</td>
                        <td>{{item.quantity}}</td>
                        <td>{{item.unit}}</td>
                      </tr>
                    </tbody>
                  </table>
                      
         
                <vue-bar-graph :points=mydata :show-y-axis="true"
                                    :show-x-axis="true"
                                    :width="1200"
                                    :height="600"
                                    :show-values="true"/>
     
                  
              </div>
            </div>

            <div class="mb-3 mt-3" v-else>
              <input type="text" name="input"
                     v-model="foods" class="form-control" placeholder="Enter Food name"/>
              <input type="text" name="input"
                     v-model="inger" class="form-control" placeholder="How many ingredients"/>
                <span class="">Food name : "chicken", "lamb", "garlic" (any 1 or combination seperated by comma)</span><br/>
                <span class="">ingredients : 3-4 (min-max)</span><br/>
              <button type="submit" class="btn btn-primary m-3"
                       @click="get_recipe(foods, inger)">Get Recipe</button>

                <div class="row mt-3" v-if='recipeList !=""'>
                  <div class="card" 
                       style="width: 18rem;"
                       v-for="item in recipeList"
                       :key="item.id">
                    <img :src=item.recipe.images.THUMBNAIL.url class="card-img-top">
                    <div class="card-body">
                      <h5 class="card-title">{{item.recipe.label}}</h5>
                      <p class="card-text">Diet : {{item.recipe.dietLabels}}</p>
                      <p class="card-text">mealType : {{item.recipe.mealType}}</p>
                      <p class="card-text">dishType : {{item.recipe.dishType}}</p>
                      <p class="card-text">calories : {{item.recipe.calories}}</p>
                      <p class="card-text">Weight : {{item.recipe.totalWeight}}</p>
                      <a :href=item.recipe.url class="btn btn-primary">Goto Full recipe</a>
                    </div>
                  </div>
              </div>
            </div>
        </div>
    </div>
    
  </section>

  
</template>
<script>

import axios from 'axios';
import VueBarGraph from 'vue-bar-graph';


export default {
  name: 'Diet',
  components: {
    VueBarGraph,
},
  data(){
      return {
          nutritionURL: "https://api.edamam.com/api/nutrition-data",
          recipeURL: "https://api.edamam.com/api/recipes/v2",
          appID:"d9a8d3d2",
          appKey:"1abf30192c308a5611926b8c424bc159",
          nutritionList:"",
          recipeList:"",
          nutrition: true,
          foods:"",
          inger:"",
          mydata: []
      }
  },
  methods:{
      find_nutrition_value(food){
        // construct API URL
        var url = `${this.nutritionURL}?app_id=${this.appID}&app_key=${this.appKey}&nutrition-type=cooking&ingr=${food}`
        // API Request
        axios.get(url)
        .then(response => {
          this.nutritionList = response.data;
          this.process_chart(this.nutritionList.totalDaily);
          })
        .catch(error => {
          console.log(error);
        })
      },
      get_recipe(food, inger){
        //construct URL
        var url = `${this.recipeURL}?type=public&q=${food}&app_id=8014d851&app_key=0c317450f0ccce8229bb4d469607cfce&inger=${inger}`
        axios.get(url)
        .then(response => {
            this.recipeList = response.data.hits
        });
      },
      change_status(value){
        if(value== 'nut'){
          this.foods = "";
          this.nutrition = true;
          this.recipeList = "";
          this.mydata=[];
        }else{
          this.foods = "";
           this.nutrition = false;
          this.nutritionList = "";
        }
      },
      process_chart(data){

       Object.entries(data).forEach(entry => {
          const [key, item] = entry;
            console.log(key);
            var dataPoints = {label: item.label, value: item.quantity}
            this.mydata.push(dataPoints);
        });
      }
      
  }
}
</script>