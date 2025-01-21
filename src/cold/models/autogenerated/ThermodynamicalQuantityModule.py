
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISO80000CategorisedModule import ISO80000Categorised







class ThermodynamicalQuantity(ISO80000Categorised):
    """
    Class representing the `ThermodynamicalQuantity` entity, which inherits from:
    - ISO80000Categorised

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_dae32a4a_d8da_4047_81b0_36a9713fdce1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ThermodynamicalQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ThermodynamicalQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_dae32a4a_d8da_4047_81b0_36a9713fdce1',
    
    class_name='ThermodynamicalQuantity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_dae32a4a_d8da_4047_81b0_36a9713fdce1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ThermodynamicalQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    