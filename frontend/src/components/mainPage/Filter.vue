<template>
    <div class="filter-box">
        <div>
            <button type="button" class="filter-button active" id="filter-active">Otvorené</button>
            <button type="button" class="filter-button" id="filter-available">Dostupné menu</button>
            <button type="button" class="filter-button" id="filter-vegetarian">🌱</button>
            <button type="button" class="filter-button" id="filter-meat">🍗</button>
        </div>
        <hr>
        <div>
            <button type="button" class="filter-button" id="filter-price">Cena</button>
            <button type="button" class="filter-button active" id="filter-rating">Hodnotenie</button>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Filter'
}
</script>