---
bgp_config:
  as_number: "65252"
  bgp:
    log_neighbor_changes: true
    router_id:
      address: "10.0.20.2"
  redistribute:
    - connected:
        metric: 0
  neighbor:
    - address: "10.10.0.30"
      remote_as: "65252"
    - address: "10.10.0.25"
      remote_as: "65252"
    - address: "10.11.11.10"
      remote_as: "65253"
