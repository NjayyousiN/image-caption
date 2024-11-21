/* 
    This file contains the function that is used to interact with the server to call the API for caption generation.
    This function is called by the components in the frontend to send requests to the server.
*/
"use server";

export async function generateCaption(image: FormData ): Promise<{ english_caption: string; arabic_caption: string }> {
    // Send a POST request to the server to generate a caption for the image
    const response = await fetch('http://127.0.0.1:8000/generate-caption', {
        method: 'POST',
        body: image,
    });
    const data = await response.json();
    return data;
}