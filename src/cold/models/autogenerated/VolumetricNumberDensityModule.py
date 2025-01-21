
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReciprocalVolumeModule import ReciprocalVolume







class VolumetricNumberDensity(ReciprocalVolume):
    """
    Class representing the `VolumetricNumberDensity` entity, which inherits from:
    - ReciprocalVolume

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_90a39fcb_5087_451e_a92e_ce0adc6d80f1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VolumetricNumberDensity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VolumetricNumberDensity(
    
    class_iri='https://w3id.org/emmo#EMMO_90a39fcb_5087_451e_a92e_ce0adc6d80f1',
    
    class_name='VolumetricNumberDensity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_90a39fcb_5087_451e_a92e_ce0adc6d80f1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VolumetricNumberDensity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    