import { Link } from "react-router-dom";

export default function DocumentCard({ document }) {
  return (
    <div className="bg-white rounded-xl shadow p-5 mt-5">

      <h3 className="text-xl font-semibold">
        {document.original_filename}
      </h3>

      <p className="text-gray-600 mt-2">
        Status: {document.status}
      </p>

      <p className="text-gray-600">
        Type: {document.document_type}
      </p>

      <Link to={`/document/${document.id}`}>
        <button
          className="
            mt-4
            bg-blue-600
            text-white
            px-5
            py-2
            rounded-lg
            hover:bg-blue-700
          "
        >
          View
        </button>
      </Link>

    </div>
  );
}