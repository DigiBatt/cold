
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicsBasedModelModule import PhysicsBasedModel







class MaterialsModel(PhysicsBasedModel):
    """
    Class representing the `MaterialsModel` entity, which inherits from:
    - PhysicsBasedModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_90f18cf0_1225_4c64_b5f8_f65cd7f992c5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MaterialsModel'`
        - **Alias**: `class_name`
    
    - `hasSpatialSlice` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialSlice`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MaterialsModel(
    
    class_iri='https://w3id.org/emmo#EMMO_90f18cf0_1225_4c64_b5f8_f65cd7f992c5',
    
    class_name='MaterialsModel',
    
    hasSpatialSlice="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_90f18cf0_1225_4c64_b5f8_f65cd7f992c5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MaterialsModel',
        alias="class_name"
    )
    
    hasSpatialSlice: Optional[str] = Field(
        None,
        alias="hasSpatialSlice"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    