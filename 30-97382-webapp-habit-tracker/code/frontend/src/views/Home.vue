<template>
  <section class="mt-3">
    <p>Good Habit Tracker.</p>

    <div v-if="isLoggedIn" id="logout">
      <p id="logout">Click <a href="/mh">here</a> to view all Mental health entry.</p>
    </div>
    <p v-else>
      <span><a href="/register">Register</a></span>
      <span> or </span>
      <span><a href="/login">Log In</a></span>
    </p>
  </section>
</template>
<script>

export default {
  name: 'Home',
  computed : {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
}
</script>