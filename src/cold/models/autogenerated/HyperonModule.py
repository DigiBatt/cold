
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BaryonModule import Baryon







class Hyperon(Baryon):
    """
    Class representing the `Hyperon` entity, which inherits from:
    - Baryon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f87e79eb_f549_4a06_9c27_a3d1412444c6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Hyperon'`
        - **Alias**: `class_name`
    
    - `hasProperPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasProperPart`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Hyperon(
    
    class_iri='https://w3id.org/emmo#EMMO_f87e79eb_f549_4a06_9c27_a3d1412444c6',
    
    class_name='Hyperon',
    
    hasProperPart="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f87e79eb_f549_4a06_9c27_a3d1412444c6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Hyperon',
        alias="class_name"
    )
    
    hasProperPart: Optional[str] = Field(
        None,
        alias="hasProperPart"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    