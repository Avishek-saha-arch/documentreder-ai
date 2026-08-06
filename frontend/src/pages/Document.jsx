import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../api/api";

export default function Document() {
  const { id } = useParams();

  const [document, setDocument] = useState(null);
  const [aiData, setAiData] = useState(null);
  useEffect(() => {
    loadDocument();
  }, []);

  const loadDocument = async () => {
    const response = await api.get(`/documents/${id}`);
    setDocument(response.data);

    if (response.data.extracted_data) {
        setAiData(
            JSON.parse(response.data.extracted_data)
        );
    }
  };

  if (!document) {
    return <h2 className="p-10">Loading...</h2>;
  }

  return (
    <div className="max-w-5xl mx-auto p-8">

      <h1 className="text-3xl font-bold">
        {document.original_filename}
      </h1>

      <p className="mt-4">
        <b>Status:</b> {document.status}
      </p>

      <p>
        <b>Type:</b> {document.document_type}
      </p>

      <div className="mt-8 bg-white shadow rounded-xl p-6">

        <h2 className="text-2xl font-bold mb-4">
          OCR Text
        </h2>

        <pre className="whitespace-pre-wrap">
          {document.raw_text || "No OCR text yet."}
        </pre>

      </div>
        <div className="mt-8 bg-white shadow rounded-xl p-6">

        <h2 className="text-2xl font-bold mb-4">
            AI Extracted Data
        </h2>

       {aiData ? (

        <div className="space-y-4">

            <div>
            <h3 className="font-semibold">
                Document Type
            </h3>

            <p>{aiData.document_type}</p>
            </div>

            <div>
            <h3 className="font-semibold">
                Summary
            </h3>

            <p>{aiData.summary}</p>
            </div>

        </div>

        ) : (

        <p>No AI data yet.</p>

        )}

        </div> 
    </div>
  );
}