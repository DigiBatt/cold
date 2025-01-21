
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CondensedMatterPhysicsQuantityModule import CondensedMatterPhysicsQuantity



from .LengthModule import Length







class CoherenceLength(CondensedMatterPhysicsQuantity, Length):
    """
    Class representing the `CoherenceLength` entity, which inherits from:
    - CondensedMatterPhysicsQuantity, Length

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_477042ef_3173_49b2_a264_0e3270733f8c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CoherenceLength'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CoherenceLength(
    
    class_iri='https://w3id.org/emmo#EMMO_477042ef_3173_49b2_a264_0e3270733f8c',
    
    class_name='CoherenceLength',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_477042ef_3173_49b2_a264_0e3270733f8c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CoherenceLength',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    