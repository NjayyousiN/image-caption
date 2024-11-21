"use client";

import { useState } from "react";
import { Upload, ImageIcon, AlertCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { generateCaption } from "@/services/actions";

export default function ImageCaptioningUI() {
    const [image, setImage] = useState<string | null>(null);
    const [caption, setCaption] = useState<string | null>(null);

    const handleImageUpload = async (
        event: React.ChangeEvent<HTMLInputElement>
    ) => {
        const file = event.target.files?.[0];
        if (file) {
            const formData = new FormData();
            formData.append("file_upload", file);
            const caption = await generateCaption(formData);
            setImage(URL.createObjectURL(file));
            setCaption(caption);     
            console.log(caption);
        }
    };

    return (
        <div className="min-h-screen bg-gradient-to-br from-purple-400 via-pink-500 to-red-500 flex items-center justify-center p-4">
            <Card className="w-full max-w-md bg-white rounded-xl shadow-2xl">
                <CardContent className="p-6">
                    <h1 className="text-3xl font-bold text-center mb-6 text-gray-800">
                        Image Captioning
                    </h1>
                    <div className="space-y-4">
                        <div className="flex items-center justify-center w-full">
                            <label
                                htmlFor="file_upload"
                                className="flex flex-col items-center justify-center w-full h-64 border-2 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100"
                            >
                                <div className="flex flex-col items-center justify-center pt-5 pb-6">
                                    <Upload className="w-10 h-10 mb-3 text-gray-400" />
                                    <p className="mb-2 text-sm text-gray-500">
                                        <span className="font-semibold">
                                            Click to upload
                                        </span>{" "}
                                        or drag and drop
                                    </p>
                                    <p className="text-xs text-gray-500">
                                        PNG, JPG or GIF (MAX. 800x400px)
                                    </p>
                                </div>
                                <Input
                                    id="file_upload"
                                    type="file"
                                    className="hidden"
                                    accept="image/*"
                                    onChange={handleImageUpload}
                                />
                            </label>
                        </div>
                        {image && (
                            <div className="mt-4">
                                <img
                                    src={image}
                                    alt="Uploaded"
                                    className="w-full h-auto rounded-lg"
                                />
                            </div>
                        )}
                        {caption && (
                            <div className="mt-4 p-4 bg-blue-100 rounded-lg">
                                <div className="flex items-start">
                                    <ImageIcon className="w-5 h-5 mr-2 text-blue-500" />
                                    <p className="text-blue-700">{caption}</p>
                                </div>
                            </div>
                        )}
                        {!image && !caption && (
                            <div className="mt-4 p-4 bg-yellow-100 rounded-lg">
                                <div className="flex items-start">
                                    <AlertCircle className="w-5 h-5 mr-2 text-yellow-500" />
                                    <p className="text-yellow-700">
                                        Upload an image to generate a caption.
                                    </p>
                                </div>
                            </div>
                        )}
                    </div>
                </CardContent>
            </Card>
        </div>
    );
}
