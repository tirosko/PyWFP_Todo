const recipeForm = document.querySelector("#recipe-form");
const recipeList = document.querySelector("#recipe-list");
const recipeCount = document.querySelector("#recipe-count");
const emptyMessage = document.querySelector("#empty-message");
const undoMessage = document.querySelector("#undo-message");
const undoDeleteButton = document.querySelector("#undo-delete-button");

let recipes = [
    { name: "Rezance s miso a maslom", description: "Jemné rezance premiešané s miso pastou, maslom, sezamom a trochou limetkovej šťavy." },
    { name: "Hrianka s pečenými paradajkami", description: "Pomaly pečené paradajky, našľahaná ricotta, bazalka a čierne korenie na kváskovom chlebe." },
    { name: "Chrumkavý cícerový šalát", description: "Chrumkavý korenený cícer s uhorkou, bylinkami a sviežou citrónovou zálievkou." }
];
let deletedRecipe = null;

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
                <span class="recipe-number">RECEPT ${String(index + 1).padStart(2, "0")}</span>
                <button class="delete-button" type="button" data-index="${index}" aria-label="Odstrániť ${escapeHtml(recipe.name)}">Odstrániť</button>
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
    const index = Number(deleteButton.dataset.index);
    const [recipe] = recipes.splice(index, 1);
    deletedRecipe = { recipe, index };
    undoMessage.hidden = false;
    renderRecipes();
});

undoDeleteButton.addEventListener("click", () => {
    if (!deletedRecipe) return;
    recipes.splice(deletedRecipe.index, 0, deletedRecipe.recipe);
    deletedRecipe = null;
    undoMessage.hidden = true;
    renderRecipes();
});

renderRecipes();