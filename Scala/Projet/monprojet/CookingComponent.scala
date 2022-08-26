

trait CookingComponent{
    this: RecipeComponent =>

    val cooker: Cooker

    class CookerImpl extends Cooker {
        override def cook(what: String): Food = {
            val recipeText = recipe.findRecipe(what)
            Food(s"We just cooked $what using the following recipe: '$recipeText'.")
	  }
    }
}