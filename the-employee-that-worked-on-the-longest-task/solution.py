def worker_with_longest_task(n: int, logs: list[list[int]]) -> int:
    """Return the id of the employee that worked the longest single task.

    Args:
        n: Number of employees.
        logs: List of [employee_id, leave_time] pairs, sorted by leave_time.

    Returns:
        Employee id with the longest task (smallest id on tie).
    """
    best_id = logs[0][0]
    best_duration = logs[0][1]
    prev_time = logs[0][1]

    for i in range(1, len(logs)):
        duration = logs[i][1] - prev_time
        if duration > best_duration or (duration == best_duration and logs[i][0] < best_id):
            best_id = logs[i][0]
            best_duration = duration
        prev_time = logs[i][1]

    return best_id
