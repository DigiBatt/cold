
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ConventionalModule import Conventional







class Coded(Conventional):
    """
    Class representing the `Coded` entity, which inherits from:
    - Conventional

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_7286b164_df4c_4c14_a4b5_d41ad9c121f3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Coded'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Coded(
    
    class_iri='https://w3id.org/emmo#EMMO_7286b164_df4c_4c14_a4b5_d41ad9c121f3',
    
    class_name='Coded',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_7286b164_df4c_4c14_a4b5_d41ad9c121f3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Coded',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    