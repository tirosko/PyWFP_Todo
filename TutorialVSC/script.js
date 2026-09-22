const recipeForm = document.querySelector("#recipe-form");
const recipeList = document.querySelector("#recipe-list");
const recipeCount = document.querySelector("#recipe-count");
const emptyMessage = document.querySelector("#empty-message");

let recipes = [
    { name: "Miso butter noodles", description: "Silky noodles tossed with miso, butter, sesame, and a squeeze of lime." },
    { name: "Roasted tomato toast", description: "Slow-roasted tomatoes, whipped ricotta, basil, and black pepper on sourdough." },
    { name: "Crispy chickpea salad", description: "Crunchy spiced chickpeas with cucumber, herbs, and a bright lemon dressing." }
];

function renderRecipes() {
    recipeList.innerHTML = "";
    recipeCount.textContent = recipes.length;
    emptyMessage.hidden = recipes.length > 0;

    recipes.forEach((recipe, index) => {
        const card = document.createElement("article");
        card.className = "recipe-card";
        card.innerHTML = `
            <div>
                <h3>${escapeHtml(recipe.name)}</h3>
                <p>${escapeHtml(recipe.description)}</p>
            </div>
            <div class="card-footer">
                <span class="recipe-number">RECIPE ${String(index + 1).padStart(2, "0")}</span>
                <button class="delete-button" type="button" data-index="${index}" aria-label="Delete ${escapeHtml(recipe.name)}">Delete</button>
            </div>
        `;
        recipeList.appendChild(card);
    });
}

function escapeHtml(value) {
    return value.replace(/[&<>'"]/g, (character) => ({
        "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#039;", '"': "&quot;"
    }[character]));
}

recipeForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const formData = new FormData(recipeForm);
    recipes.unshift({
        name: formData.get("name").trim(),
        description: formData.get("description").trim()
    });
    recipeForm.reset();
    renderRecipes();
});

recipeList.addEventListener("click", (event) => {
    const deleteButton = event.target.closest(".delete-button");
    if (!deleteButton) return;
    recipes.splice(Number(deleteButton.dataset.index), 1);
    renderRecipes();
});

renderRecipes();