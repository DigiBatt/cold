
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISO80000CategorisedModule import ISO80000Categorised



from .BaseQuantityModule import BaseQuantity



from .InternationalSystemOfQuantityModule import InternationalSystemOfQuantity







class ISQBaseQuantity(ISO80000Categorised, BaseQuantity, InternationalSystemOfQuantity):
    """
    Class representing the `ISQBaseQuantity` entity, which inherits from:
    - ISO80000Categorised, BaseQuantity, InternationalSystemOfQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1a4c1a97_88a7_4d8e_b2f9_2ca58e92dde4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ISQBaseQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ISQBaseQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_1a4c1a97_88a7_4d8e_b2f9_2ca58e92dde4',
    
    class_name='ISQBaseQuantity',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1a4c1a97_88a7_4d8e_b2f9_2ca58e92dde4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ISQBaseQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    