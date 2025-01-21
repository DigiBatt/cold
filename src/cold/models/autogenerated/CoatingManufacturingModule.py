
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MergingManufacturingModule import MergingManufacturing







class CoatingManufacturing(MergingManufacturing):
    """
    Class representing the `CoatingManufacturing` entity, which inherits from:
    - MergingManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_92028373_3a43_4b80_9a69_caca22df3918'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CoatingManufacturing'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CoatingManufacturing(
    
    class_iri='https://w3id.org/emmo#EMMO_92028373_3a43_4b80_9a69_caca22df3918',
    
    class_name='CoatingManufacturing',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_92028373_3a43_4b80_9a69_caca22df3918',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CoatingManufacturing',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    