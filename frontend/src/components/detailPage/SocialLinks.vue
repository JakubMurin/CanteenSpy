<template>
  <div class="social-links-box">
    <a :href="location" class="social-link">
      <img src="@/assets/images/geo-alt-fill.svg" alt="Location">
    </a>
    <a :href="share" class="social-link">
      <img src="@/assets/images/share-fill.svg" alt="Share">
    </a>
    <a :href="website" class="social-link">
      <img src="@/assets/images/globe2.svg" alt="Website URL">
    </a>
  </div>
</template>

<script>
export default {
  name: 'SocialLinks',
  props: [
    'location',
    'share',
    'website'
  ],
};

</script>
