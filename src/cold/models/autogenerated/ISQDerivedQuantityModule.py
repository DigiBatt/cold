
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DerivedQuantityModule import DerivedQuantity



from .InternationalSystemOfQuantityModule import InternationalSystemOfQuantity







class ISQDerivedQuantity(DerivedQuantity, InternationalSystemOfQuantity):
    """
    Class representing the `ISQDerivedQuantity` entity, which inherits from:
    - DerivedQuantity, InternationalSystemOfQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2946d40b_24a1_47fa_8176_e3f79bb45064'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ISQDerivedQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ISQDerivedQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_2946d40b_24a1_47fa_8176_e3f79bb45064',
    
    class_name='ISQDerivedQuantity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2946d40b_24a1_47fa_8176_e3f79bb45064',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ISQDerivedQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    