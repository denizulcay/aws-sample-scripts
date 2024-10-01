from google.cloud import videointelligence

video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.Feature.LABEL_DETECTION]
with open('/Users/denizulcay/code/local/aws-sample-scripts/resources/videos/tornado.mp4', 'rb') as f:
    imput_content = f.read()

request = videointelligence.AnnotateVideoRequest(
    features=features,
    input_content=imput_content
)
operation = video_client.annotate_video(
    request=request
)
print("\nProcessing video for label annotations:")

result = operation.result(timeout=180)
print("\nFinished processing.")

# first result is retrieved because a single video was processed
segment_labels = result.annotation_results[0].segment_label_annotations
for i, segment_label in enumerate(segment_labels):
    print("Video label description: {}".format(segment_label.entity.description))
    for category_entity in segment_label.category_entities:
        print(
            "\tLabel category description: {}".format(category_entity.description)
        )

    for i, segment in enumerate(segment_label.segments):
        start_time = (
                segment.segment.start_time_offset.seconds
                + segment.segment.start_time_offset.microseconds / 1e6
        )
        end_time = (
                segment.segment.end_time_offset.seconds
                + segment.segment.end_time_offset.microseconds / 1e6
        )
        positions = "{}s to {}s".format(start_time, end_time)
        confidence = segment.confidence
        print("\tSegment {}: {}".format(i, positions))
        print("\tConfidence: {}".format(confidence))
    print("\n")