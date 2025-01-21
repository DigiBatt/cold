
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EMMOModule import EMMO







class Collection(EMMO):
    """
    Class representing the `Collection` entity, which inherits from:
    - EMMO

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2d2ecd97_067f_4d0e_950c_d746b7700a31'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Collection'`
        - **Alias**: `class_name`
    
    - `hasMember` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMember`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Collection(
    
    class_iri='https://w3id.org/emmo#EMMO_2d2ecd97_067f_4d0e_950c_d746b7700a31',
    
    class_name='Collection',
    
    hasMember="example_value",
    
    conceptualisation="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2d2ecd97_067f_4d0e_950c_d746b7700a31',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Collection',
        alias="class_name"
    )
    
    hasMember: Optional[str] = Field(
        None,
        alias="hasMember"
    )
    
    conceptualisation: Optional[str] = Field(
        None,
        alias="conceptualisation"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    