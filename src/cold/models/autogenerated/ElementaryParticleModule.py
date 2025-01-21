
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CausalPathModule import CausalPath



from .PhysicalParticleModule import PhysicalParticle







class ElementaryParticle(CausalPath, PhysicalParticle):
    """
    Class representing the `ElementaryParticle` entity, which inherits from:
    - CausalPath, PhysicalParticle

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_7b79b2ac_3cf2_4d3b_8cdc_bcabb59d869e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElementaryParticle'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElementaryParticle(
    
    class_iri='https://w3id.org/emmo#EMMO_7b79b2ac_3cf2_4d3b_8cdc_bcabb59d869e',
    
    class_name='ElementaryParticle',
    
    elucidation="example_value",
    
    conceptualisation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_7b79b2ac_3cf2_4d3b_8cdc_bcabb59d869e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElementaryParticle',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    conceptualisation: Optional[str] = Field(
        None,
        alias="conceptualisation"
    )
    

    
    

    

    