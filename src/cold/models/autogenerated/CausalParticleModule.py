
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ItemModule import Item







class CausalParticle(Item):
    """
    Class representing the `CausalParticle` entity, which inherits from:
    - Item

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6c03574f_6daa_4488_a970_ee355cca2530'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CausalParticle'`
        - **Alias**: `class_name`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CausalParticle(
    
    class_iri='https://w3id.org/emmo#EMMO_6c03574f_6daa_4488_a970_ee355cca2530',
    
    class_name='CausalParticle',
    
    definition="example_value",
    
    conceptualisation="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6c03574f_6daa_4488_a970_ee355cca2530',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CausalParticle',
        alias="class_name"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    conceptualisation: Optional[str] = Field(
        None,
        alias="conceptualisation"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    