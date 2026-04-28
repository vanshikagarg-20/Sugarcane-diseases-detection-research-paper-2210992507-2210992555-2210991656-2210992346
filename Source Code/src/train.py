import yaml
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from model import build_model

# Load config
with open("config.yaml") as f:
    config = yaml.safe_load(f)

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30,
    zoom_range=0.2,
    horizontal_flip=True
)

val_datagen = ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory(
    config['paths']['train_dir'],
    target_size=(224,224),
    batch_size=config['batch_size'],
    class_mode='categorical'
)

val_data = val_datagen.flow_from_directory(
    config['paths']['val_dir'],
    target_size=(224,224),
    batch_size=config['batch_size'],
    class_mode='categorical'
)

model = build_model(train_data.num_classes)

model.compile(
    optimizer=Adam(learning_rate=config['learning_rate']),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=config['epochs']
)

model.save(config['paths']['model_output'] + "model.h5")