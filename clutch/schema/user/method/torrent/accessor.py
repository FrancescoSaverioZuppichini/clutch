from typing import Set, Sequence
from clutch.compat import Literal, TypedDict

from clutch.schema.user.method.shared import IdsArg

AccessorField = Literal[
    "activity_date",
    "added_date",
    "bandwidth_priority",
    "comment",
    "corrupt_ever",
    "creator",
    "date_created",
    "desired_available",
    "done_date",
    "download_dir",
    "downloaded_ever",
    "download_limit",
    "download_limited",
    "edit_date",
    "error",
    "error_string",
    "eta",
    "eta_idle",
    "files",
    "file_stats",
    "hash_string",
    "have_unchecked",
    "have_valid",
    "honors_session_limits",
    "id",
    "is_finished",
    "is_private",
    "is_stalled",
    "labels",
    "left_until_done",
    "magnet_link",
    "manual_announce_time",
    "max_connected_peers",
    "metadata_percent_complete",
    "name",
    "peer_limit",
    "peers",
    "peers_connected",
    "peers_from",
    "peers_getting_from_us",
    "peers_sending_to_us",
    "percent_done",
    "pieces",
    "piece_count",
    "piece_size",
    "priorities",
    "queue_position",
    "rate_download",
    "rate_upload",
    "recheck_progress",
    "seconds_downloading",
    "seconds_seeding",
    "seed_idle_limit",
    "seed_idle_mode",
    "seed_ratio_limit",
    "seed_ratio_mode",
    "size_when_done",
    "start_date",
    "status",
    "trackers",
    "tracker_stats",
    "total_size",
    "torrent_file",
    "uploaded_ever",
    "upload_limit",
    "upload_limited",
    "upload_ratio",
    "wanted",
    "webseeds",
    "webseeds_sending_to_us",
]

TorrentAccessorFields = Set[AccessorField]


class TorrentAccessorArgumentsOptional(TypedDict, total=False):
    ids: IdsArg
    format: Literal["objects", "table"]


class TorrentAccessorArguments(TorrentAccessorArgumentsOptional):
    fields: TorrentAccessorFields


field_keys: Sequence[str] = [
    "activity_date",
    "added_date",
    "bandwidth_priority",
    "comment",
    "corrupt_ever",
    "creator",
    "date_created",
    "desired_available",
    "done_date",
    "download_dir",
    "downloaded_ever",
    "download_limit",
    "download_limited",
    "edit_date",
    "error",
    "error_string",
    "eta",
    "eta_idle",
    "files",
    "file_stats",
    "hash_string",
    "have_unchecked",
    "have_valid",
    "honors_session_limits",
    "id",
    "is_finished",
    "is_private",
    "is_stalled",
    "labels",
    "left_until_done",
    "magnet_link",
    "manual_announce_time",
    "max_connected_peers",
    "metadata_percent_complete",
    "name",
    "peer_limit",
    "peers",
    "peers_connected",
    "peers_from",
    "peers_getting_from_us",
    "peers_sending_to_us",
    "percent_done",
    "pieces",
    "piece_count",
    "piece_size",
    "priorities",
    "queue_position",
    "rate_download",
    "rate_upload",
    "recheck_progress",
    "seconds_downloading",
    "seconds_seeding",
    "seed_idle_limit",
    "seed_idle_mode",
    "seed_ratio_limit",
    "seed_ratio_mode",
    "size_when_done",
    "start_date",
    "status",
    "trackers",
    "tracker_stats",
    "total_size",
    "torrent_file",
    "uploaded_ever",
    "upload_limit",
    "upload_limited",
    "upload_ratio",
    "wanted",
    "webseeds",
    "webseeds_sending_to_us",
]
