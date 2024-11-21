"use server";

export async function generateCaption(image: FormData ): Promise<string> {
    const response = await fetch('http://127.0.0.1:8000/generate-caption', {
        method: 'POST',
        body: image,
    });
    const data = await response.json();
    return data;
}