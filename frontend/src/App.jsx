import { useEffect, useState } from "react";
import API from "./api";
import { useRef } from "react";

function App() {

  const [records, setRecords] = useState([]);
  const [summary, setSummary] = useState({});
  const [search, setSearch] = useState("");
  const [statusFilter, setStatusFilter] = useState("ALL");
  const [showSuspicious, setShowSuspicious] = useState(false);
  const [auditLogs, setAuditLogs] = useState([]);
  const sapFileRef = useRef();
  const utilityFileRef = useRef();
  const travelFileRef = useRef();

  useEffect(() => {
    fetchRecords();
    fetchSummary();
    fetchAuditLogs();
  }, []);

  const fetchRecords = async () => {
    const response = await API.get("/records/");
    setRecords(response.data);
  };

  const fetchSummary = async () => {
    const response = await API.get("/dashboard/summary/");
    setSummary(response.data);
  };

  const fetchAuditLogs = async () => {
    const response = await API.get("/audit-logs/");
    setAuditLogs(response.data);
  };

  const approveRecord = async (id) => {
    await API.post(`/records/${id}/approve/`);
    fetchRecords();
    fetchSummary();
    fetchAuditLogs();
  };

  const rejectRecord = async (id) => {
    await API.post(`/records/${id}/reject/`);
    fetchRecords();
    fetchSummary();
    fetchAuditLogs();
  };

  const uploadFile = async (type, file) => {

  if (!file) {
    alert("Please select a file");
    return;
  }

  const formData = new FormData();

  formData.append("file", file);

  try {

    await API.post(
      `/upload/${type}/`,
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );

    alert(`${type.toUpperCase()} upload successful`);

    fetchRecords();
    fetchSummary();

  } catch (error) {

    console.error(error);

    alert("Upload failed");
  }
};

const filteredRecords = records.filter((record) => {

  const matchesSearch =
    record.activity_type
      .toLowerCase()
      .includes(search.toLowerCase());

  const matchesStatus =
    statusFilter === "ALL"
      ? true
      : record.status === statusFilter;

  const matchesSuspicious =
    showSuspicious
      ? record.suspicious_flag
      : true;

  return (
    matchesSearch &&
    matchesStatus &&
    matchesSuspicious
  );
});

  return (
    <div className="min-h-screen w-full bg-gray-100 p-8">

      <h1 className="text-4xl font-bold mb-8">
        Breathe ESG Dashboard
      </h1>

      <div className="bg-white rounded-xl shadow p-6 mb-8">

  <h2 className="text-2xl font-semibold mb-4">
    Upload ESG Data
  </h2>

  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">

    <div className="border rounded-lg p-4">

      <h3 className="font-semibold mb-3">
        SAP Fuel Data
      </h3>

      <input
        type="file"
        ref={sapFileRef}
        className="mb-3"
      />

      <button
        onClick={() =>
          uploadFile(
            "sap",
            sapFileRef.current.files[0]
          )
        }
        className="bg-blue-500 text-white px-4 py-2 rounded"
      >
        Upload SAP CSV
      </button>

    </div>

    <div className="border rounded-lg p-4">

      <h3 className="font-semibold mb-3">
        Utility Electricity Data
      </h3>

      <input
        type="file"
        ref={utilityFileRef}
        className="mb-3"
      />

      <button
        onClick={() =>
          uploadFile(
            "utility",
            utilityFileRef.current.files[0]
          )
        }
        className="bg-yellow-500 text-white px-4 py-2 rounded"
      >
        Upload Utility CSV
      </button>

    </div>

    <div className="border rounded-lg p-4">

      <h3 className="font-semibold mb-3">
        Travel Platform Data
      </h3>

      <input
        type="file"
        ref={travelFileRef}
        className="mb-3"
      />

      <button
        onClick={() =>
          uploadFile(
            "travel",
            travelFileRef.current.files[0]
          )
        }
        className="bg-purple-500 text-white px-4 py-2 rounded"
      >
        Upload Travel CSV
      </button>

    </div>

  </div>

</div>

      <div className="grid grid-cols-5 gap-4 mb-8">

        <div className="bg-white p-4 rounded-xl shadow">
          <h2 className="text-gray-500">Total</h2>
          <p className="text-3xl font-bold">
            {summary.total_records || 0}
          </p>
        </div>

        <div className="bg-white p-4 rounded-xl shadow">
          <h2 className="text-gray-500">Approved</h2>
          <p className="text-3xl font-bold">
            {summary.approved_records || 0}
          </p>
        </div>

        <div className="bg-white p-4 rounded-xl shadow">
          <h2 className="text-gray-500">Rejected</h2>
          <p className="text-3xl font-bold">
            {summary.rejected_records || 0}
          </p>
        </div>

        <div className="bg-white p-4 rounded-xl shadow">
          <h2 className="text-gray-500">Pending</h2>
          <p className="text-3xl font-bold">
            {summary.pending_records || 0}
          </p>
        </div>

        <div className="bg-white p-4 rounded-xl shadow">
          <h2 className="text-gray-500">Suspicious</h2>
          <p className="text-3xl font-bold text-red-500">
            {summary.suspicious_records || 0}
          </p>
        </div>

      </div>
      
        <div className="bg-white rounded-xl shadow p-4 mb-6">

  <div className="flex flex-col md:flex-row gap-4">

    <input
      type="text"
      placeholder="Search activity..."
      value={search}
      onChange={(e) => setSearch(e.target.value)}
      className="border rounded px-4 py-2 w-full"
    />

    <select
      value={statusFilter}
      onChange={(e) => setStatusFilter(e.target.value)}
      className="border rounded px-4 py-2"
    >
      <option value="ALL">All Status</option>
      <option value="PENDING">Pending</option>
      <option value="APPROVED">Approved</option>
      <option value="REJECTED">Rejected</option>
    </select>

    <label className="flex items-center gap-2">

      <input
        type="checkbox"
        checked={showSuspicious}
        onChange={() =>
          setShowSuspicious(!showSuspicious)
        }
      />

      Suspicious Only

    </label>

  </div>

</div>

      <div className="bg-white rounded-xl shadow p-4 overflow-x-auto">

        <table className="min-w-full">

          <thead>
            <tr className="border-b">

              <th className="p-3 text-left">Activity</th>
              <th className="p-3 text-left">Scope</th>
              <th className="p-3 text-left">Quantity</th>
              <th className="p-3 text-left">Emission</th>
              <th className="p-3 text-left">Status</th>
              <th className="p-3 text-left">Validation</th>
              <th className="p-3 text-left">Actions</th>

            </tr>
          </thead>

          <tbody>

            {filteredRecords.map((record) => (

              <tr
                key={record.id}
                className={
                  record.suspicious_flag
                    ? "bg-red-100 border-b"
                    : "border-b"
                }
              >

                <td className="p-3">
                  {record.activity_type}
                </td>

                <td className="p-3">
                  {record.scope}
                </td>

                <td className="p-3">
                  {record.quantity} {record.unit}
                </td>

                <td className="p-3">
                  {record.emission_value} kgCO2e
                </td>

                <td className="p-3">

                  <span
                    className={
                      record.status === "APPROVED"
                        ? "bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm font-medium"
                        : record.status === "REJECTED"
                          ? "bg-red-100 text-red-700 px-3 py-1 rounded-full text-sm font-medium"
                          : "bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full text-sm font-medium"
                    }
                  >
                    {record.status}
                  </span>

                  {
                    record.locked && (
                      <div className="text-xs text-gray-500 mt-1">
                        Locked for audit
                      </div>
                    )
                  }

                </td>

                <td className="p-3 text-sm text-red-500">
                  {record.validation_message}
                </td>

                <td className="p-3 flex gap-2">

                  <button
                    disabled={record.locked}
                    onClick={() => approveRecord(record.id)}
                    className={
                      record.locked
                        ? "bg-gray-400 text-white px-3 py-1 rounded cursor-not-allowed"
                        : "bg-green-500 text-white px-3 py-1 rounded"
                    }
                  >
                    Approve
                  </button>

                  <button
                    disabled={record.locked}
                    onClick={() => rejectRecord(record.id)}
                    className={
                      record.locked
                        ? "bg-gray-400 text-white px-3 py-1 rounded cursor-not-allowed"
                        : "bg-red-500 text-white px-3 py-1 rounded"
                    }
                  >
                    Reject
                  </button>

                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>
    <div className="bg-white rounded-xl shadow p-6 mt-8">

  <h2 className="text-2xl font-semibold mb-4">
    Audit History
  </h2>

  <div className="overflow-x-auto">

    <table className="min-w-full">

      <thead>

        <tr className="border-b">

          <th className="text-left p-3">
            Field
          </th>

          <th className="text-left p-3">
            Old Value
          </th>

          <th className="text-left p-3">
            New Value
          </th>

          <th className="text-left p-3">
            Timestamp
          </th>

        </tr>

      </thead>

      <tbody>

        {auditLogs.map((log) => (

          <tr
            key={log.id}
            className="border-b"
          >

            <td className="p-3">
              {log.field_name}
            </td>

            <td className="p-3">
              {log.old_value}
            </td>

            <td className="p-3">
              {log.new_value}
            </td>

            <td className="p-3">
              {new Date(
                log.edited_at
              ).toLocaleString()}
            </td>

          </tr>

        ))}

      </tbody>

    </table>

  </div>

</div>
    </div>
  );
}

export default App;