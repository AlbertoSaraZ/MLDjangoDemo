from MemeDetector.MLModels.resnet152memes import ResNet152Memes


def process_new_image(sender, instance, **kwargs):
    if not instance.was_processed:
        print("processing new image")
        resnet = ResNet152Memes()
        (meme_confidence, no_meme_confidence) = resnet.predict(instance.image.path)
        instance.meme_confidence = round(meme_confidence, 3)
        instance.no_meme_confidence = round(no_meme_confidence, 3)
        instance.was_processed = True
        if (instance.meme_confidence > 0.5 and instance.submitted_as_meme) or\
                (instance.no_meme_confidence > 0.5 and not instance.submitted_as_meme):
            instance.correct_prediction = True
        instance.save()
    else:
        print("image processed")
