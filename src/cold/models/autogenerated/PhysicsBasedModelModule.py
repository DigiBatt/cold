
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CausalSystemModule import CausalSystem



from .MathematicalModelModule import MathematicalModel



from .MathematicalConstructModule import MathematicalConstruct







class PhysicsBasedModel(CausalSystem, MathematicalModel, MathematicalConstruct):
    """
    Class representing the `PhysicsBasedModel` entity, which inherits from:
    - CausalSystem, MathematicalModel, MathematicalConstruct

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b29fd350_39aa_4af7_9459_3faa0544cba6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhysicsBasedModel'`
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
    obj = PhysicsBasedModel(
    
    class_iri='https://w3id.org/emmo#EMMO_b29fd350_39aa_4af7_9459_3faa0544cba6',
    
    class_name='PhysicsBasedModel',
    
    hasSpatialSlice="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b29fd350_39aa_4af7_9459_3faa0544cba6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhysicsBasedModel',
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
    

    
    

    

    