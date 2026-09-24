async function generateStory() {

    const storyIdea = document.getElementById("storyIdea").value.trim();
    const loading = document.getElementById("loading");
    const result = document.getElementById("result");
    const story = document.getElementById("story");

    if (!storyIdea) {
        alert("Please enter a story idea!");
        return;
    }

    loading.style.display = "block";
    result.style.display = "none";

    try {

        const response = await fetch("/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                story_idea: storyIdea
            })
        });

        const data = await response.json();

        if (data.success) {
            story.textContent = data.story;
            result.style.display = "block";
        } else {
            alert(data.message || "Something went wrong.");
        }

    } catch (error) {

        console.error(error);

        alert(
            "Unable to connect to ComicCraft server."
        );

    } finally {

        loading.style.display = "none";
    }
}
